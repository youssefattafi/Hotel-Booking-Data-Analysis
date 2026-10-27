# Hotel Booking Data Analysis 🏨

Exploratory data analysis of hotel booking records using Python, Pandas, and Jupyter Notebook.

## Project overview

This project explores hotel reservation data to understand booking activity, cancellations, customer and market segments, room assignments, guest origins, and average daily rates (ADR). The goal is to practice cleaning real-world tabular data and communicating insights through descriptive statistics and visualizations.

## Analysis covered

- Load and inspect hotel booking records
- Identify missing values and duplicate records
- Explore booking characteristics and cancellation patterns
- Analyze guest country of origin, hotel types, and booking channels/market segments
- Compare reserved and assigned room types
- Investigate ADR and guest arrival patterns

## Files

| File | Description |
|---|---|
| [Hotel_booking_Analysis_Shan_Singh.ipynb](Hotel_booking_Analysis_Shan_Singh.ipynb) | Original exploratory analysis notebook |
| [hotel_bookings.csv](hotel_bookings.csv) | Hotel bookings dataset |
| [requirements.txt](requirements.txt) | Python packages needed for typical notebook analyses |

## Run locally

1. Download or clone the repository.
2. Install requirements with `python -m pip install -r requirements.txt`.
3. Start Jupyter with `jupyter notebook`.
4. Open `Hotel_booking_Analysis_Shan_Singh.ipynb`.
5. **Update any local Windows-style absolute CSV path** in the notebook to a portable relative path:

   ```python
   df = pd.read_csv("hotel_bookings.csv")
   ```

6. Run notebook cells in order. Depending on the notebook's imports, additional packages may be required.

## Technologies

Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook

## Portfolio context and limitations

This repository contains exploratory analysis, not a deployed predictive model. Insights, charts, and numerical findings should be interpreted from the executed notebook; this README does not claim specific measured outcomes without verification.

**Attribution:** The source notebook is named `Hotel_booking_Analysis_Shan_Singh.ipynb`. If it was adapted from Shan Singh's tutorial or another learning resource, retain the original author's credit and add a link to the exact source once identified. Distinguish your own changes from original tutorial material.

## Next improvements

- Make CSV loading portable without a manual path edit
- Document validated findings from notebook outputs
- Add a cleaned-up notebook with clear methodology and chart descriptions
- Add a business recommendations section tied to observed results
