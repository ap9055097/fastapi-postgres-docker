from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()
@router.get("/{id}", response_model=schemas.GridDB)
def read_grid(
    *,
    db: Session = Depends(deps.get_db),
    id: Any,
) -> Any:
    """
    Get grid by ID.
    """
    grid = db.query(models.Grid).filter(models.Grid.gridID == id).first()
    if not grid:
        raise HTTPException(status_code=404, detail="Grid not found")
    return grid


@router.get("/", response_model=List[schemas.GridDB])
def read_grids(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve grid.
    """
    return db.query(models.Grid).offset(skip).limit(limit).all()