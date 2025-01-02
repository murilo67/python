#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Leitura do salário do funcionário
salario = float(input("\033[1;32mDigite o salário do funcionário: R$ \033[0m"))

# Cálculo do aumento de 15%
aumento = 0.15 * salario

# Cálculo do novo salário com aumento
novo_salario = salario + aumento

# Exibição do resultado
print("\033[1;36m--- Cálculo de Aumento de Salário ---\033[0m")
print("\033[1;34mSalário atual: R$ {:.2f}\033[0m".format(salario))
print("\033[1;34mAumento de 15%: R$ {:.2f}\033[0m".format(aumento))
print("\033[1;34mNovo salário com aumento: R$ {:.2f}\033[0m".format(novo_salario))
