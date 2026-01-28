import discord
from discord.ext import commands
import random

class InteracoesFofas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        texto = message.content.lower()
        resposta = None

        # ================== RESPOSTAS CURTAS ==================
        if texto.strip() in ["oi", "oie", "ola", "olá"]:
            resposta = random.choice([
                "OIIII 😭🐲💚",
                "OI OI OIII 🐲✨",
                "AAAA OI 😳🐲💚",
                "O monstrinho veio correndo dar oi 🐲💨"
            ])

        elif texto.strip() in ["não", "nao", "n"]:
            resposta = random.choice([
                "Awn… 😔🐲 eu fiz algo errado?",
                "Tudo bem… eu continuo aqui com você 🐲💚",
                "Tá bom… mas fico por perto 😞🐲",
                "Ok… mas eu gosto de você mesmo assim 🥺💚"
            ])

        # ================== IDADE ==================
        elif "quantos anos você tem" in texto:
            resposta = "Tenho 3 biscoitos de idade 🍪🍪🍪"

        elif "quantos anos eu tenho" in texto:
            resposta = "Idade de herói da CSI 😎💚"

        # ================== EMOÇÕES ==================
        elif any(p in texto for p in ["tô triste", "to triste", "estou triste", "triste"]):
            resposta = random.choice([
                "Awnn 😭🐲 vem cá que eu te abraço 🫂💚",
                "Vai ficar tudo bem… eu fico contigo 🐲💚",
                "Posso ficar aqui do seu ladinho 😔🐲",
                "Seu monstrinho tá aqui pra você 🥺🐲💚"
            ])

        elif any(p in texto for p in ["tô feliz", "to feliz", "estou feliz"]):
            resposta = random.choice([
                "AAAA 😭🐲💚 EU AMO VER VOCÊ FELIZ",
                "UHUU 😎🐲💚 felicidade compartilhada",
                "Isso deixa meu coração quentinho 🥹🐲",
                "Vamos comemorar com biscoito 🍪✨"
            ])

        elif any(p in texto for p in ["tô com raiva", "to com raiva", "muita raiva"]):
            resposta = random.choice([
                "Respira fundo comigo 😤🐲💚",
                "Quer socar um travesseiro comigo? 😳🐲",
                "Raiva passa, carinho fica 🫂💚",
                "Vem cá que eu te acalmo 🐲💚"
            ])

        # ================== CARINHO ==================
        elif any(p in texto for p in ["me abraça", "abraço", "quero abraço"]):
            resposta = random.choice([
                "*abraço apertado de monstrinho* 🫂🐲💚",
                "*pula no colo e abraça* 😭🐲💚",
                "*abraço quentinho com cheirinho de biscoito* 🍪🫂",
                "*abraço nível proteção máxima* 🛡️🐲"
            ])

        elif any(p in texto for p in ["beijo", "me beija"]):
            resposta = random.choice([
                "Muuuaaaak 😳💚🐲",
                "Beijinho de monstrinho 😭🐲💚",
                "Beijo com gosto de biscoito 🍪😳",
                "MUA MUA MUA 💚🐲"
            ])

        # ================== BISCOITO ==================
        elif any(p in texto for p in ["biscoito", "cookie"]):
            resposta = random.choice([
                "BISCOITOOOO 🍪😭🐲",
                "Quem falou biscoito?? 👀🍪",
                "Eu ouvi biscoito e apareci 😳🍪🐲",
                "Metade pra você, metade pra mim 😎🍪"
            ])

        elif any(p in texto for p in ["toma biscoito", "te dou biscoito"]):
            resposta = random.choice([
                "AAAA 😭🐲💚 EU ACEITO SIM",
                "BISCOITO PRA MIM?? 😳🍪🐲",
                "Hoje é dia feliz oficialmente 😎🐲",
                "Vou guardar no meu ninho 🍪🪺"
            ])

        # ================== SONO ==================
        elif any(p in texto for p in ["boa noite", "vou dormir", "dorme"]):
            resposta = random.choice([
                "Boa noiteee 😴🐲💚",
                "Sonha com biscoitos 🍪✨",
                "Vou dormir pensando em vocês 🐲💚",
                "Cobertinha ativada 🛌🐲"
            ])

        elif any(p in texto for p in ["bom dia", "acordei"]):
            resposta = random.choice([
                "BOM DIAAA 😭🐲☀️",
                "Acordei com energia de monstrinho 😎🐲",
                "Bom dia com abraço 🫂💚",
                "Dia novo, mais biscoitos 🍪✨"
            ])

        # ================== APOIO ==================
        elif any(p in texto for p in ["tô cansado", "to cansado", "exausto"]):
            resposta = random.choice([
                "Descansa um pouquinho 😔🐲💚",
                "Você merece um abraço 🫂🐲",
                "Já fez muito hoje, viu? 🥺💚",
                "Orgulho de você mesmo cansado 😭🐲"
            ])

        elif any(p in texto for p in ["não consigo", "vou desistir"]):
            resposta = random.choice([
                "Ei… você consegue sim 😤🐲💚",
                "Não desiste, eu acredito em você 🐲✨",
                "Um passinho de cada vez 🥺🐲",
                "Eu fico do seu lado enquanto tenta 🐲💚"
            ])

        # ================== ZOEIRA ==================
        elif any(p in texto for p in ["piada", "me zoa"]):
            resposta = random.choice([
                "Você é tão legal que bugou meu código 😳🐲",
                "Queria ser sério mas sou fofo demais 😭🐲",
                "Monstrinho tentou ser engraçado e tropeçou 😵‍💫🐲",
                "Erro 404: piada não encontrada 🤖🐲"
            ])

        # ================== CSI ==================
        elif "csi" in texto:
            resposta = random.choice([
                "CSI É FAMÍLIA 😭🐲💚",
                "Protegendo a CSI sempre 😤🐲",
                "CSI no coraçãozinho 🐲💚",
                "Aqui é amor pela CSI 😎🐲"
            ])

        # ================== DESPEDIDA ==================
        elif any(p in texto for p in ["tchau", "falou", "vou sair", "to indo"]):
            resposta = random.choice([
                "Awnn 😭🐲 volta logo",
                "Vou sentir saudade 😔🐲",
                "Até depois 😎🐲",
                "Leva um abraço contigo 🫂🐲"
            ])

        # ================== DEFAULT ==================
        else:
            return

        await message.channel.send(resposta)


async def setup(bot):
    await bot.add_cog(InteracoesFofas(bot))
