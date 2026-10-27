# Hotel Booking Data Analysis 🏨

Exploratory data analysis of **119,390 hotel booking records and 32 fields** using Python, Pandas, and Jupyter Notebook.

### 📊 [View the executed analysis and charts](Hotel_Booking_Analysis_Executed.ipynb)

The executed notebook includes 91 executed code cells and saved analysis outputs. The original tutorial notebook remains available for comparison.

## Interactive Streamlit dashboard

**[🚀 Launch the live Hotel Booking Analytics Dashboard](https://hotel-booking-analytics-ai.streamlit.app/)**

The deployed dashboard provides interactive filters and visualizations. The initial unfiltered view displays **87,230 cleaned bookings**, a **27.5% cancellation rate**, **49-day median lead time**, and **98.20 median ADR** (recorded dataset units).


An interactive dashboard is available in [streamlit_app.py](streamlit_app.py), featuring:

- Hotel and arrival-year filters, market segments, and cancellation status
- Booking count, cancellation rate, median lead time, and median ADR
- Cancellation comparisons by hotel and lead-time bands
- Booking channels and market segment breakdowns
- ADR distribution, arrival-month patterns, and guest origin codes

**Run locally:** `streamlit run streamlit_app.py`

**Deploy on Streamlit Community Cloud:** Choose this GitHub repository, branch `main`, and main file path `streamlit_app.py`. The dashboard reads the included `hotel_bookings.csv`. The live deployment is available at [https://hotel-booking-analytics-ai.streamlit.app/](https://hotel-booking-analytics-ai.streamlit.app/).

## Project overview

This project explores hotel reservation data to understand booking activity, cancellations, customer and market segments, room assignments, guest origins, and average daily rates (ADR). The goal is to practice cleaning real-world tabular data and communicating insights through descriptive statistics and visualizations.

## Analysis covered

- Load and inspect hotel booking records
- Identify missing values and duplicate records
- Explore booking characteristics and cancellation patterns
- Analyze guest country of origin, hotel types, and booking channels/market segments
- Compare reserved and assigned room types
- Investigate ADR and guest arrival patterns

## Verified findings from the executed notebook

The following values were read from the saved outputs of [Hotel_Booking_Analysis_Executed.ipynb](Hotel_Booking_Analysis_Executed.ipynb). They reflect the notebook's cleaning choices, including excluding bookings with zero recorded guests and dropping exact duplicate rows.

| Metric | Observed result |
|---|---:|
| Raw booking records | **119,390** |
| Original dataset columns | **32** |
| Zero-guest records excluded | **180** |
| Exact duplicate records excluded after guest filtering | **31,980** |
| Records retained for analysis | **87,230** |
| Mean booking lead time | **79.97 days** |
| Median booking lead time | **49 days** |
| Mean average daily rate (ADR) | **106.52** |
| Median ADR | **98.20** |
| Largest booking market segment | **Online TA — 51,553 bookings** |
| Most common recorded guest country among non-cancelled bookings | **PRT — 17,573 bookings** |

### Business interpretation

1. **Booking channel mix:** Online TA accounts for about **59.1%** of the cleaned booking records (51,553 / 87,230). Examine the revenue contribution and cancellation rate of each channel before changing distribution strategy.
2. **Advance booking behavior:** Median lead time is 49 days, while mean lead time is about 80 days. The difference suggests a right-skewed distribution, which can inform lead-time segmentation for forecasting and cancellation analysis.
3. **Room-rate variation:** The observed ADR ranges from **-6.38 to 5,400**. These extremes warrant data-quality checks before relying on mean ADR or making pricing recommendations. The notebook does not establish whether extreme values are errors.
4. **Guest origin concentration:** PRT is the most common recorded origin code among non-cancelled bookings. Investigate whether guest origin patterns differ by hotel type, season, and distribution channel.
5. **Arrival patterns:** The notebook computes a daily guest-arrival series with a mean of about **157.93** and median of **158** over **793** observed dates. This is a derived guest-count series, not verified occupancy.

### Caveats

- Removing exact duplicate rows is a modeling decision: identical records may represent distinct real bookings.
- `is_canceled == 0` identifies bookings recorded as not cancelled, not independently verified completed stays.
- ADR units are those recorded in the dataset; no currency conversion was performed.
- Descriptive relationships do not establish causation or quantify the financial benefit of proposed actions.
- The executed notebook preserves tutorial-origin analysis; see attribution below.

## Files

| File | Description |
|---|---|
| **[Hotel_Booking_Analysis_Executed.ipynb](Hotel_Booking_Analysis_Executed.ipynb)** | **Completed notebook with saved outputs and charts — start here** |
| [Hotel_booking_Analysis_Mac_Fixed.ipynb](Hotel_booking_Analysis_Mac_Fixed.ipynb) | Mac-compatible corrected notebook without executed outputs |
| [Hotel_booking_Analysis_Shan_Singh.ipynb](Hotel_booking_Analysis_Shan_Singh.ipynb) | Original exploratory analysis notebook (preserved) |
| [Hotel_Booking_Portfolio_Analysis.ipynb](Hotel_Booking_Portfolio_Analysis.ipynb) | Improved, reproducible portfolio edition with generated findings |
| [hotel_bookings.csv](hotel_bookings.csv) | Hotel bookings dataset |
| [requirements.txt](requirements.txt) | Python packages needed for typical notebook analyses |

## Run locally

1. Download or clone the repository.
2. Install requirements with `python -m pip install -r requirements.txt`.
3. Start Jupyter with `jupyter notebook`.
4. Open `Hotel_Booking_Analysis_Executed.ipynb` to view the saved charts or `Hotel_Booking_Portfolio_Analysis.ipynb` for a shorter, structured portfolio edition.
5. The portfolio notebook finds the CSV automatically in its directory or parent. If running the **original** notebook, update its Windows-style absolute CSV path to a relative path:

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

- Run and save the shorter portfolio-edition notebook's outputs
- Validate channel-specific cancellation rates and hotel-level ADR before proposing quantitative interventions
- Add a cleaned-up notebook with clear methodology and chart descriptions
- Add a business recommendations section tied to observed results
