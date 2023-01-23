import pandas as pd
import geopandas as gpd
import plotly.express as px


def df_to_gdf(df: pd.DataFrame):
    df1 = df.copy()
    gdf = gpd.GeoDataFrame(df1, geometry=gpd.points_from_xy(df1.Longitude, df1.Latitude))
    gdf.drop(columns=['Longitude', 'Latitude'], inplace=True)
    return gdf


def plot_cities(gdf: gpd.GeoDataFrame):
    gdf1 = gdf.copy()

    fig = px.scatter_mapbox(gdf1,
                            lat=gdf1.geometry.y,
                            lon=gdf1.geometry.x,
                            hover_name='Region',
                            zoom=11,
                            color='Coast',
                            # size=gdf1.SIZE,
                            size_max=7,
                            center=dict(lat=-33.43, lon=-70.59),
                            title='Ciudades en USA y UK')

    fig.update_layout(
        height=800,
        mapbox_style="open-street-map"
    )

    fig.show()
    # fig.write_html('./output/maps/ciudades.html', auto_open=False)
