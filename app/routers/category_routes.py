from fastapi import APIRouter, Depends, HTTPException
from app.schemas.category_schema import CategoryReturn, CategoryCreate, CategoryUpdate, CategoryDeleteReturn
from app.db_connection import get_db_session, local_session
from sqlalchemy.orm import Session
from app.models import Category
import logging
from app.utils.category_utils import check_existing_category
from typing import List

logger = logging.getLogger('app')
router = APIRouter()


# endpoint to retrieve a category by its slug
@router.get('/slug/{category_slug}', response_model=CategoryReturn, status_code=200)
def category_by_slug(category_slug: str, db: Session = Depends(get_db_session)):
    try:
        category = db.query(Category).filter(Category.slug == category_slug).first()

        if not category:
            raise HTTPException(status_code=404, detail='Category does not exists!!')
        return category
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unexpected error while creating category: {e}')
        raise HTTPException(status_code=500, detail='Internal server error')


# endpoint to retrieve all categories
@router.get('/', response_model=List[CategoryReturn])
def get_categories(db: Session = Depends(get_db_session)):
    try:
        categories = db.query(Category).all()
        return categories
    except Exception as e:
        logger.error(f'Unexpected error while retrieving categories: {e}')
        raise HTTPException(status_code=500, detail='Internal server error')


# handling /category post request
@router.post('/', response_model=CategoryReturn, status_code=201)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db_session)):

    try:
        check_existing_category(db, category_data)
        new_category = Category(**category_data.model_dump())
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f'Unexpected error while creating category: {e}')
        raise HTTPException(status_code=500, detail='Internal server error')


# endpoint to update an existing category
@router.put('/{category_id}', response_model=CategoryReturn, status_code=201)
def update_category(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db_session)):
    try:
        category = db.query(Category).filter(Category.id == category_id).first()

        if not category:
            raise HTTPException(status_code=404, detail='Category does not exists!!')

        for key, value in category_data.model_dump().items():
            setattr(category, key, value)
        db.commit()
        db.refresh(category)
        return None
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unexpected error while creating category: {e}')
        raise HTTPException(status_code=500, detail='Internal server error')


# endpoint to update an existing category
@router.delete('/{category_id}', response_model=CategoryDeleteReturn, status_code=200)
def delete_category(category_id: int, db: Session = Depends(get_db_session)):
    try:
        category = db.query(Category).filter(Category.id == category_id).first()

        if not category:
            raise HTTPException(status_code=404, detail='Category does not exists!!')

        db.delete(category)
        db.commit()
        return category
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unexpected error while creating category: {e}')
        raise HTTPException(status_code=500, detail='Internal server error')
