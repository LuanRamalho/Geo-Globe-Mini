import leafmap.foliumap as leafmap

# Criamos o mapa já limitando o zoom máximo seguro
m = leafmap.Map(
    center=[-22.9519, -43.2105],
    zoom=15,
    max_zoom=18,
    tiles=None  # Remove a camada padrão para não gerar conflito
)

# 1. Camada de Imagem de Satélite (Esri World Imagery)
leafmap.folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Satélite",
    max_zoom=18
).add_to(m)

# 2. Camada de Rótulos (Nomes de ruas/locais transparentes por cima)
leafmap.folium.TileLayer(
    tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}{r}.png",
    attr="CartoDB",
    name="Rótulos",
    max_zoom=18
).add_to(m)

# Marcador no Cristo Redentor
m.add_marker(
    location=[-22.9519, -43.2105],
    popup="Rio de Janeiro - Cristo Redentor"
)

# Salva o mapa final
m.to_html("mapa_rio.html")