import time
from telethon.sync import TelegramClient
from telethon import events
import re

API_ID = 23389175
API_HASH = 'd0cb06afef29304f536529862ccdc2a7'
PHONE_NUMBER = '+5533998307878'

def main():
    while True:
        try:
            client = TelegramClient('MyMoob', API_ID, API_HASH)

            @client.on(events.NewMessage(chats=[-1001744454246]))  # ID do grupo
            async def ler_mensagem(event):
                mensagem = event.message
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
                        await client.send_message(-1001878753028, resposta)  # Envia a primeira mensagem modificada para o grupo de destino

                        # Modifica a segunda linha
                        segunda_linha_otc = segunda_linha + "-OTC"
                        resposta_otc = numero + segunda_linha_otc  # Concatena o número modificado com a segunda linha modificada
                        await client.send_message(-1001878753028, resposta_otc)  # Envia a segunda mensagem modificada para o grupo de destino

            async def run_client():
                await client.start(phone=PHONE_NUMBER)
                await client.run_until_disconnected()

            with client:
                client.loop.run_until_complete(run_client())

        except Exception as e:
            # Imprime a mensagem de erro
            print(f"Ocorreu um erro: {str(e)}")

        # Aguarda um intervalo de tempo antes de reiniciar o código
        # para evitar um loop infinito sem pausas
        time.sleep(5)  # Tempo em segundos

if __name__ == "__main__":
    main()
