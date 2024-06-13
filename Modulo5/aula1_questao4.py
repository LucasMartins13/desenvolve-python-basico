from datetime import datetime

agora = datetime.now()
data_hora_formatada = f"{agora.day:02d}/{agora.month:02d}/{agora.year} {agora.hour:02d}:{agora.minute:02d}"
print(f"Data e Hora atuais: {data_hora_formatada}")
