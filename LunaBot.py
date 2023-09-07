import discord
from discord.ext import commands
import pyjokes
import datetime
import youtube_dl
import random

token = '************************************' #mytoken

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='hora')
async def get_current_time(ctx):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    await ctx.send(f'La hora actual es: {current_time}')

@bot.command(name='fecha')
async def get_current_date(ctx):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    await ctx.send(f'La fecha de hoy es: {current_date}')

@bot.command(name='abrir')
async def open_link(ctx, link):
    await ctx.send(f'Aquí tienes el enlace: {link}')

@bot.command(name='comando')
async def custom_command(ctx, command_name):
    if command_name == 'instagram':
        await ctx.send('Puedes seguirme en Instagram en: @ginacastorena0407')
    elif command_name == 'chiste':
        chiste_aleatorio = pyjokes.get_joke()
        await ctx.send(chiste_aleatorio)

datos_musica = [
    'El instrumento más antiguo conocido es una flauta hecha de hueso, que tiene aproximadamente 35,000 años de antigüedad.',
    'La canción más reproducida en la historia de Spotify es "Shape of You" de Ed Sheeran.',
    'El piano fue inventado por Bartolomeo Cristofori en Italia alrededor de 1700.'
    'La canción "Bohemian Rhapsody" de Queen es conocida por ser una de las canciones más largas en la historia de la música pop, con una duración de más de seis minutos.'
    'El término "rock and roll" se originó en la década de 1950 y se cree que fue acuñado por el disc-jockey Alan Freed.'
    'Wolfgang Amadeus Mozart comenzó a componer música a la edad de cinco años y compuso más de 600 obras a lo largo de su vida.'
    'El compositor alemán Ludwig van Beethoven comenzó a perder la audición en su juventud, pero continuó componiendo música notable incluso después de quedarse completamente sordo.'
    'El primer reproductor de discos compactos (CD) fue lanzado al mercado en 1982 por Sony y Philips.'
    'La guitarra eléctrica fue popularizada por músicos como Chuck Berry y Jimi Hendrix en la década de 1950 y 1960.'
    'El álbum más vendido de todos los tiempos es "Thriller" de Michael Jackson, con más de 66 millones de copias vendidas en todo el mundo.'
]

datos_arte = [
    'La Mona Lisa, pintada por Leonardo da Vinci, es una de las obras de arte más famosas del mundo.',
    'El arte abstracto se caracteriza por el uso de formas y colores sin representación figurativa.',
    'El famoso pintor Vincent van Gogh cortó su propia oreja en un episodio de enfermedad mental.'
    'El cuadro "La noche estrellada" de Vincent van Gogh, pintado en 1889, es una de las obras más icónicas del arte moderno.'
    'El impresionismo, un movimiento artístico del siglo XIX, se caracteriza por la representación de la luz y el color en lugar de los detalles precisos.'
    'La escultura "El Pensador" de Auguste Rodin es una de las obras de arte más famosas del mundo y representa a un hombre profundamente absorto en sus pensamientos.'
    'La pintura "La última cena" de Leonardo da Vinci fue creada entre 1495 y 1498 y se encuentra en el convento de Santa Maria delle Grazie en Milán, Italia.'
    'El artista español Pablo Picasso es conocido por haber co-fundado el movimiento cubista y por su versatilidad en diferentes estilos artísticos.'
    'El surrealismo, un movimiento artístico del siglo XX, se caracteriza por representaciones de mundos imaginarios y oníricos.'
]

datos_historia = [
    'La Revolución Francesa comenzó en 1789 y condujo a la caída de la monarquía francesa.',
    'La Gran Muralla China fue construida a lo largo de varios siglos y tiene una longitud de más de 21,000 millas.',
    'La Segunda Guerra Mundial duró desde 1939 hasta 1945 y fue un conflicto global que involucró a muchas naciones.'
    'La Gran Muralla China tiene una longitud de más de 21,000 millas (33,800 kilómetros) y fue construida a lo largo de varios siglos.'
    'El antiguo Egipto es conocido por construir las pirámides de Giza, que son algunas de las estructuras más antiguas y grandes del mundo.'
    'La Primera Guerra Mundial se libró entre 1914 y 1918 y fue uno de los conflictos más mortales de la historia, con millones de muertos y heridos.'
    'La Revolución Industrial, que marcó el inicio de la industrialización masiva, comenzó en Gran Bretaña en el siglo XVIII.'
    'El Imperio Romano existió durante más de 1,000 años, desde el 27 a.C. hasta el 476 d.C.'
    'La Revolución Rusa de 1917 llevó al derrocamiento del gobierno zarista y al establecimiento de la Unión Soviética.'
    'Marco Polo, el famoso explorador veneciano, viajó por Asia durante el siglo XIII y escribió sobre sus experiencias en "El libro de las maravillas del mundo".'
]

datos_tecnologia = [
    "La inteligencia artificial y el aprendizaje automático están revolucionando múltiples industrias.",
    "La computación cuántica utiliza principios de la mecánica cuántica para cálculos extremadamente rápidos.",
    "La tecnología 5G ofrece velocidades de Internet móvil mucho más rápidas y menor latencia.",
    "La Internet de las Cosas (IoT) conecta dispositivos cotidianos a través de Internet.",
    "Los robots están desempeñando un papel cada vez más importante en la fabricación y la medicina.",
    "La realidad virtual (RV) sumerge a las personas en entornos virtuales.",
    "La realidad aumentada (RA) superpone información digital en el mundo real.",
    "La tecnología blockchain es la base de las criptomonedas como Bitcoin y Ethereum.",
    "La impresión 3D permite crear objetos tridimensionales a partir de diseños digitales.",
    "Los vehículos autónomos, como coches sin conductor, están siendo probados en todo el mundo."
]

@bot.command(name='dato')
async def custom_command(ctx, command_name):
    if command_name == 'arte':
        # Selecciona un dato aleatorio sobre arte de la lista
        dato_aleatorio = random.choice(datos_arte)
        await ctx.send(dato_aleatorio)
    elif command_name == 'historia':
        # Selecciona un dato aleatorio sobre historia de la lista
        dato_aleatorio = random.choice(datos_historia)
        await ctx.send(dato_aleatorio)
    elif command_name == 'musica':
        # Selecciona un dato aleatorio sobre música de la lista
        dato_aleatorio = random.choice(datos_musica)
        await ctx.send(dato_aleatorio)
    elif command_name == 'tecnologia':
        # Selecciona un dato aleatorio sobre música de la lista
        dato_aleatorio = random.choice(datos_tecnologia)
        await ctx.send(dato_aleatorio)


@bot.command(name='reproducir')
async def play_youtube(ctx, url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        voice_client.play(discord.FFmpegPCMAudio(url2))

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

bot.run(token)
