#%%
#Cria e reescreve o arquivo
txt = "Meu novo arquivo\n"

nome_arquivo ="historia_02.txt"

with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)

#%%
#Adiciona caracteres novos
txt2 = "Meu novo arquivo de texto \n"

nome_arquivo ="historia_02.txt"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt2)