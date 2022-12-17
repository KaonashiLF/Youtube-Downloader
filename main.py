from downloader import youtube_functions

yt_link = r"https://www.youtube.com/watch?v=o-wX-jiOnfI"
errorlink = 'https://www.estudarfora.org.br/cursos-online-gratuitos-de-harvard/'



youtube_functions.Download(yt_link)
youtube_functions.get_general_info(yt_link)