import leafmap.foliumap as leafmap


# Centro do mapa: Rio de Janeiro, próximo ao Cristo Redentor.
# Impede que o programa adicione um mapa-base padrão.
m = leafmap.Map(
    center=[-22.9519, -43.2105],
    zoom=15,
    max_zoom=18,
    tiles=None,
)


# Camada de imagens de satélite da Esri.
# Única camada raster adicionada ao mapa.
# A camada CartoDB que provocava o aviso foi removida.
leafmap.folium.TileLayer(
    tiles=(
        "https://server.arcgisonline.com/ArcGIS/rest/services/"
        "World_Imagery/MapServer/tile/{z}/{y}/{x}"
    ),
    attr=(
        "Tiles &copy; Esri, Maxar, Earthstar Geographics, "
        "and the GIS User Community"
    ),
    name="Satélite Esri",
    max_zoom=18,
    overlay=False,
    control=True,
    show=True,
).add_to(m)


# Marcador no Cristo Redentor.
m.add_marker(
    location=[-22.9519, -43.2105],
    popup="Rio de Janeiro - Cristo Redentor",
)


# Gera o arquivo HTML do mapa.
saida = "mapa_rio.html"
m.to_html(saida)

print(f"Mapa criado com sucesso: {saida}")
