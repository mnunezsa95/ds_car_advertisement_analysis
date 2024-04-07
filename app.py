import pandas as pd
import plotly_express as px
import streamlit as st

vehicles_df = pd.read_csv("./vehicles_data.csv")
st.title("Data Analysis for Vehicles")

# ------------------------------------------------------------------------------------------------ #
#                                              Dataset                                             #
# ------------------------------------------------------------------------------------------------ #

st.header("Vehicle Dataset")
st.dataframe(
    data=vehicles_df,
    width=None,
    height=None,
    use_container_width=False,
    hide_index=True,
    column_order=None,
    column_config=None,
)

st.write("---")

# ------------------------------------------------------------------------------------------------ #
#                                       Distribution Analysis                                      #
# ------------------------------------------------------------------------------------------------ #

st.header("Distribution Analysis")

# ----------------------------------------- Vehicle Price ---------------------------------------- #

st.subheader("Distribution of Vehicle Price")
price_dist = px.histogram(vehicles_df, x="price", nbins=50)
price_dist.update_layout(
    yaxis_title="Frequency",
    xaxis_title="Price",
    bargap=0.2,
)
price_dist.update_traces(marker_color="rgb(136, 204, 88)")
st.write(price_dist)

# ----------------------------------------- Vehicle Year ----------------------------------------- #

st.subheader("Distribution of Vehicle Year")
vehicle_year_dist = px.histogram(vehicles_df, x="model_year", nbins=200)
vehicle_year_dist.update_layout(
    yaxis_title="Frequency",
    xaxis_title="Year of Model",
    bargap=0.2,
)
st.write(vehicle_year_dist)

# ----------------------------------------- Vehicle Make ----------------------------------------- #

st.subheader("Distribution of Vehicle Make")
vehicle_make_dist = px.histogram(vehicles_df, x="make")
vehicle_make_dist.update_xaxes(tickangle=45)
vehicle_make_dist.update_layout(
    yaxis_title="Frequency",
    xaxis_title="Vehicle Make",
    bargap=0.2,
)
vehicle_make_dist.update_traces(marker_color="rgb(248, 156, 116)")
st.write(vehicle_make_dist)

# ----------------------------------------- Vehicle Model ---------------------------------------- #

st.subheader("Distribution of Vehicle Model")
number_to_display = st.slider("Number to display:", 1, 50, 25)

model_counts = vehicles_df["model"].value_counts()
top_n_models = model_counts.head(number_to_display)

vehicle_model_dist = px.histogram(x=top_n_models.index, y=top_n_models.values)
vehicle_model_dist.update_xaxes(tickangle=45)
vehicle_model_dist.update_layout(
    title_text=f"Currently Showing: Top {number_to_display}",
    yaxis_title="Frequency",
    xaxis_title="Vehicle Model",
    bargap=0.2,
)
vehicle_model_dist.update_traces(marker_color="rgb(102, 194, 165)")
st.write(vehicle_model_dist)


# ----------------------------------- Vehicle Make by Condition ---------------------------------- #

st.subheader("Distribution of Vehicle Make by Condition")
vehicle_make_cond_dist = px.histogram(vehicles_df, x="make", color="condition")
vehicle_make_cond_dist.update_layout(
    yaxis_title="Frequency",
    xaxis_title="Vehicle Make",
    height=800,
)

st.write(vehicle_make_cond_dist)

# ------------------------------------------ Paint Color ----------------------------------------- #
st.subheader("Distribution of Vehicle Paint Color")
paint_color_dist = px.histogram(vehicles_df, x="paint_color")
paint_color_dist.update_layout(
    yaxis_title="Frequency",
    xaxis_title="Vehicle Paint Color",
)
paint_color_dist.update_traces(marker_color="rgb(102, 166, 30)")

st.write(paint_color_dist)


st.write("---")

# ------------------------------------------------------------------------------------------------ #
#                                         Scatter Analysis                                         #
# ------------------------------------------------------------------------------------------------ #

st.header("Scatter Analysis")


# ----------------------------------------- Price vs Year ---------------------------------------- #

st.subheader("Price vs Year")
make_checkbox = st.checkbox(
    "Show Vehicle Make Option",
    value=False,
    key=None,
    help=None,
    on_change=None,
    args=None,
    kwargs=None,
    disabled=False,
    label_visibility="visible",
)


def show_vehicle_make():
    if make_checkbox:
        return px.scatter(
            vehicles_df,
            x="model_year",
            y="price",
            labels={"model_year": "Year", "price": "Price ($)", "make": "Vehicle Make"},
            opacity=0.7,
            color="make",
        )
    else:
        return px.scatter(
            vehicles_df,
            x="model_year",
            y="price",
            labels={
                "model_year": "Year",
                "price": "Price ($)",
            },
            opacity=0.7,
            color_discrete_sequence=["orange"],
        )


st.write(show_vehicle_make())


# ------------------------------------- Price vs Days Listed ------------------------------------- #
st.subheader("Price vs Days Listed")
price_days_listed_scatter = px.scatter(
    vehicles_df,
    x="days_listed",
    y="price",
    labels={"days_listed": "Days Listed", "price": "Price ($)"},
    opacity=0.3,
)

st.write(price_days_listed_scatter)
