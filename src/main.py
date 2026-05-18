from src.demand import Demand
from src.storage import load_data, save_data
from src.weather import get_weather

def menu():
    print("\n=== Sistema de Demanda de Comunidades ===")
    print("\nClima atual:", get_weather())
    print("1 - Criar demanda")
    print("2 - Listar demandas")
    print("3 - Atualizar status")
    print("4 - Remover demanda")
    print("5 - Sair")

def main():
    demands = load_data()

    while True:
        menu()
        choice = input("Escolha: ")

        if choice == "1":
            title = input("Título: ")
            desc = input("Descrição: ")
            category = input("Categoria: ")

            demand = Demand(title, desc, category)
            demands.append(demand.to_dict())
            save_data(demands)

        elif choice == "2":
            for d in demands:
                print(d)

        elif choice == "3":
            id_ = int(input("ID: "))
            status = input("Novo status: ")

            for d in demands:
                if d["id"] == id_:
                    d["status"] = status

            save_data(demands)

        elif choice == "4":
            id_ = int(input("ID: "))
            demands = [d for d in demands if d["id"] != id_]
            save_data(demands)

        elif choice == "5":
            break

if __name__ == "__main__":
    main()