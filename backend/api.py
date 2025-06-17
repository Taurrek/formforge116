from fastapi import FastAPI
from .athlete_comparison_api import app as athlete_comparison_app

# Create the main FastAPI instance
app = FastAPI()

# Include the athlete comparison app's router
app.include_router(athlete_comparison_app, prefix="/athlete_comparison", tags=["athlete_comparison"])
