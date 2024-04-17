import sys
sys.path.append('C:/Users/altnet/Documents/JornadaDados/ProjectVerbEnglish/verb/')
from verb import Verb

def main():
    verbo = input(f"Digite um verbo em inglês: ")

    verbo_obj = Verb(verbo)
    print("No passado (Simple Past):", verbo_obj.passado())
    print("No presente (Simple Present):", verbo_obj.presente())
    print("No futuro (Simple Future):", verbo_obj.futuro())

    print(f"\nObrigado por usar o programa!")

if __name__ == "__main__":
    main()