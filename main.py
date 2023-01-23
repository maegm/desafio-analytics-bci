import pandas as pd
import preprocess
import plots


def main():
    """
    Script que contiene los cálculos del desafío.
    :return:
    """
    filepath = './data/worldcitiespop.txt'
    # Filtrar las ciudades y países relevantes en el análisis.
    df = (
        pd.read_csv(filepath, encoding="ISO-8859-1")
        .drop_duplicates(subset=['Country', 'City', 'Region'], ignore_index=True)
        .pipe(preprocess.select_countries)
        .pipe(preprocess.define_east_and_west_coast)
    )

    # Contar las ciudades totales y las ciudad que poseen el mismo nombre en el Reino Unido
    df_inter = (
        df.merge(
            df.pipe(preprocess.usa_cities_in_uk)
            .reset_index(drop=False),
            on=['City'],
            how='left'
        )
        .groupby(['Coast'], as_index=False)[['City', 'united kingdom']].count()
    )

    # Número de habitantes en zonas urbanas de cada costa.
    df_pop = df.groupby(['Coast'], as_index=False)['Population'].sum()

    # Plotear mapa completo
    (
        df.pipe(plots.df_to_gdf)
        .pipe(plots.plot_cities)
    )


if __name__ == '__main__':
    main()

