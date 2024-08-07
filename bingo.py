import customtkinter as ctk
import tkinter as tk
import random
import time

# Lista de frases associadas a cada número
frases_75 = [
    "1. Um ótimo começo!", 
    "2. Vamos lá!", 
    "3. Continuando com energia!", 
    "4. Estamos progredindo!", 
    "5. Boa sorte!",
    "6. Excelente escolha!", 
    "7. Muito bem!", 
    "8. Continue assim!", 
    "9. Isso mesmo!", 
    "10. Ótimo trabalho!",
    "11. Você está indo bem!", 
    "12. A sorte está com você!", 
    "13. Vamos lá, continue!", 
    "14. Você está arrasando!",
    "15. Avançando com sucesso!", 
    "16. Muito próximo da vitória!", 
    "17. Bom progresso!", 
    "18. Continue firme!",
    "19. Perfeito!", 
    "20. Continue assim!", 
    "21. Ótima jogada!", 
    "22. Foco e determinação!",
    "23. Continue com esse entusiasmo!", 
    "24. Muito bem até agora!", 
    "25. Você está indo muito bem!",
    "26. Ótima escolha!", 
    "27. Continue avançando!", 
    "28. Estamos quase lá!", 
    "29. Ótima jogada!",
    "30. Isso é o que eu gosto de ver!", 
    "31. Você está no caminho certo!", 
    "32. Isso mesmo!",
    "33. Você está fazendo um ótimo trabalho!", 
    "34. Parabéns pela escolha!", 
    "35. Você está arrasando!",
    "36. Ótima escolha!", 
    "37. Continue assim!", 
    "38. Estamos quase lá!", 
    "39. Muito bem!",
    "40. Você está se saindo muito bem!", 
    "41. Parabéns!", 
    "42. Ótimo progresso!", 
    "43. Estamos avançando!",
    "44. Muito bem!", 
    "45. Continue assim!", 
    "46. Você está indo muito bem!", 
    "47. Ótimo trabalho!",
    "48. Parabéns pelo progresso!", 
    "49. Estamos indo muito bem!", 
    "50. Continue assim!",
    "51. Você está indo muito bem!", 
    "52. Muito bom!", 
    "53. Estamos quase lá!", 
    "54. Parabéns!",
    "55. Você está indo muito bem!", 
    "56. Ótimo trabalho!", 
    "57. Continue com esse entusiasmo!",
    "58. Você está se saindo bem!", 
    "59. Ótimo progresso!", 
    "60. Parabéns pelo progresso!",
    "61. Estamos avançando bem!", 
    "62. Ótima escolha!", 
    "63. Você está indo bem!",
    "64. Ótima escolha!", 
    "65. Estamos quase lá!", 
    "66. Ótimo trabalho!",
    "67. Você está indo muito bem!", 
    "68. Continue assim!", 
    "69. Muito bem!",
    "70. Você está se saindo bem!", 
    "71. Ótima escolha!", 
    "72. Estamos quase lá!",
    "73. Você está indo muito bem!", 
    "74. Parabéns pelo progresso!",
    "75. Ótima escolha!", 
] + ["Frase genérica para número {}.".format(i) for i in range(6, 76)]

frases_90 = frases_75 + [
    "76. Estamos quase lá!", 
    "77. Muito bom!",
    "78. Você está indo muito bem!", 
    "79. Ótima escolha!", 
    "80. Estamos quase lá!",
    "81. Você está se saindo bem!", 
    "82. Parabéns pelo progresso!", 
    "83. Ótima escolha!",
    "84. Muito bem!", 
    "85. Estamos quase lá!", 
    "86. Ótima escolha!",
    "87. Você está indo muito bem!", 
    "88. Ótimo trabalho!", 
    "89. Continue assim!", 
    "90. Você está indo muito bem!"
] + ["Frase genérica para número {}.".format(i) for i in range(76, 91)]

# Função para exibir a animação do sorteio
def animacao_sorteio(numero):
    for _ in range(10):
        label_numero.configure(text=str(random.randint(1, 90)), fg_color="orange")
        janela.update()
        time.sleep(0.1)
    label_numero.configure(text=str(numero), fg_color="green")

# Função para sortear um número
def sortear_numero():
    global numeros_sorteados, max_numero
    if len(numeros_sorteados) < max_numero:
        numero = random.choice([n for n in range(1, max_numero+1) if n not in numeros_sorteados])
        numeros_sorteados.add(numero)
        animacao_sorteio(numero)
        frase = frases_75[numero-1] if max_numero == 75 else frases_90[numero-1]
        label_frase.configure(text=frase)
        atualizar_historico()
    else:
        label_frase.configure(text="Todos os números já foram sorteados!")

# Função para atualizar o histórico de números sorteados
def atualizar_historico():
    historico_texto = "Números sorteados:\n" + "\n".join(map(str, sorted(numeros_sorteados)))
    label_historico.config(state=tk.NORMAL)
    label_historico.delete(1.0, tk.END)  # Limpa o texto anterior
    label_historico.insert(tk.END, historico_texto)  # Adiciona o novo texto
    label_historico.config(state=tk.DISABLED)

# Função para escolher a quantidade máxima de números
def escolher_max_numero(n):
    global max_numero, numeros_sorteados
    max_numero = n
    numeros_sorteados = set()
    label_numero.configure(text="Pressione 'Sortear'")
    label_frase.configure(text="")
    atualizar_historico()
    botao_75.configure(state="disabled")
    botao_90.configure(state="disabled")

# Configuração da janela principal
janela = ctk.CTk()
janela.title("Bingo Automático")
janela.geometry("800x600")
janela.resizable(width=False, height=False)

# Rótulos para exibir o número sorteado, a frase e o histórico
label_numero = ctk.CTkLabel(janela, text="Pressione 'Sortear'", font=("Helvetica", 48, "bold"), width=200, height=100, fg_color="blue")
label_numero.pack(pady=20)

label_frase = ctk.CTkLabel(janela, text="", font=("Helvetica", 24), width=300, height=100)
label_frase.pack(pady=20)

# Caixa de texto rolável para o histórico
frame_historico = ctk.CTkFrame(janela, width=400, height=350)
frame_historico.pack(side="right", padx=20, pady=20, fill="y")

label_historico = tk.Text(frame_historico, font=("Helvetica", 18), wrap=tk.WORD, height=15, width=30)
label_historico.pack(expand=True, fill="both")

# Botões para sortear números e escolher a quantidade máxima
botao_sortear = ctk.CTkButton(janela, text="Sortear", command=sortear_numero, font=("Helvetica", 30))
botao_sortear.pack(pady=10)

botao_75 = ctk.CTkButton(janela, text="Até 75", command=lambda: escolher_max_numero(75), font=("Helvetica", 25))
botao_75.pack(side="left", padx=20, pady=20)

botao_90 = ctk.CTkButton(janela, text="Até 90", command=lambda: escolher_max_numero(90), font=("Helvetica", 25))
botao_90.pack(side="right", padx=20, pady=20)

# Variáveis globais para armazenar números sorteados e o limite
numeros_sorteados = set()
max_numero = 75

janela.mainloop()
