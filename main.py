from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
#from database import SessionLocal, engine
from models import engine, SessionLocal

# `app = FastAPI()` creates a new instance of the FastAPI class, which is used to define and handle
# HTTP requests.
app = FastAPI()

models.Base.metadata.create_all(bind=engine)


   # This function returns a database session and ensures it is closed after use.
 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



   # This is a simple Python function that returns a JSON message "Holiday planning!" when the root URL


@app.get("/")
async def root():
    return {"message": "Holiday planning!"}

# Get new holidays endpoint
@app.post("/holidays/")
def create_holiday(holiday: schemas.HolidayCreate, db: Session = Depends(get_db)):
    db_holiday = models.Holiday(**holiday.dict())
    db.add(db_holiday)
    db.commit()
    db.refresh(db_holiday)
    return db_holiday

# Get id holidays endpoint
@app.get("/holidays/{holiday_id}", response_model=schemas.Holiday)
def read_holiday(holiday_id: int, db: Session = Depends(get_db)):
    db_holiday = db.query(models.Holiday).filter(models.Holiday.id == holiday_id).first()
    if not db_holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")
    return db_holiday

# Get all holidays endpoint
@app.get("/holidays/")
def get_holidays(db: Session = Depends(get_db)):
    return db.query(models.Holiday).all()

# Delete holiday endpoint
@app.delete("/holidays/{holiday_id}")
def delete_holiday(holiday_id: int, db: Session = Depends(get_db)):
    db_holiday = db.query(models.Holiday).filter(models.Holiday.id == holiday_id).first()
    if not db_holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")
    db.delete(db_holiday)
    db.commit()
    return {"message": "Holiday deleted"}


# Update holiday endpoint
@app.put("/holidays/{holiday_id}")
def update_holiday(holiday_id: int, holiday: schemas.HolidayUpdate, db: Session = Depends(get_db)):
    db_holiday = db.query(models.Holiday).filter(models.Holiday.id == holiday_id).first()
    if not db_holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")
    update_data = holiday.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_holiday, key, value)
    db.commit()
    db.refresh(db_holiday)
    return db_holiday