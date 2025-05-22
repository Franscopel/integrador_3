from initial_load import carga_inicial


if __name__ == "__main__":
    termo_repo, registros_encontrados = carga_inicial()

    for registro in registros_encontrados:
        termo_repo.insert_one(registro)