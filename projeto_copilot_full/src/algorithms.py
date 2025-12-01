
def soma_numeros_pares(numeros: list[int]) -> int:
    return sum(n for n in numeros if n % 2 == 0)

def eh_palindromo(texto: str) -> bool:
    t = ''.join(c.lower() for c in texto if c.isalnum())
    return t == t[::-1]

def contagem_caracteres(texto: str) -> dict[str,int]:
    d={}
    for c in texto:
        d[c]=d.get(c,0)+1
    return d

def fibonacci(n: int) -> list[int]:
    if n<=0: return []
    if n==1: return [0]
    seq=[0,1]
    while len(seq)<n:
        seq.append(seq[-1]+seq[-2])
    return seq

def ordenar_numeros(nums: list[int]) -> list[int]:
    return sorted(nums)
