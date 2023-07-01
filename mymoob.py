import telebot
import re

CHAVE_API = "6164395739:AAHICp3QyTIrylUqz9XGmuyYmhdP_05E0_A"
ID_GRUPO_ORIGEM = -1001875493150
ID_GRUPO_DESTINO = -1001878753028

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(func=lambda mensagem: mensagem.chat.id == ID_GRUPO_ORIGEM)
def ler_mensagem(mensagem):
    linhas = mensagem.text.split("\n")[:2]  # Obtém apenas as duas primeiras linhas

    if len(linhas) >= 1:  # Verifica se há pelo menos uma linha
        primeira_linha = linhas[0]
        primeiro_numero = re.search(r'\d+', primeira_linha)

        if primeiro_numero is not None:  # Verifica se foi encontrado um número na primeira linha
            primeiro_numero = primeiro_numero.group()
            numero = f"M{primeiro_numero};"

            segunda_linha = linhas[1]
            segunda_linha = re.sub(r"[🟩🟥]", "", segunda_linha)  # Remove o quadrado verde e o quadrado vermelho
            segunda_linha = segunda_linha.strip()  # Remove os espaços em branco no início e no fim

            resposta = numero + segunda_linha  # Concatena o número modificado com a segunda linha
            bot.send_message(ID_GRUPO_DESTINO, resposta)  # Envia a mensagem modificada para o grupo de destino

bot.polling()