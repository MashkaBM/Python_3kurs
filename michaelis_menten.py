import json
import sys
from argparse import ArgumentParser


def rapid(S, E0, Km, k):
    v = S*k*E0/(Km+S)
    return (v)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-S', type=float) #концентрация субстрата, моль/л
    parser.add_argument('-E0', type=float) #начальная концентрация фермента, моль/л
    parser.add_argument('-Km', type=float) #константа Михаэлиса, моль/л 
    parser.add_argument('-k', type=float) #константа скорости реакции превращения фермент-субстратного комплекса в фермент и продукт, 1/с 
    parser.add_argument ('--save_file', type=str, required=False)

    args = parser.parse_args() 
    
    v = rapid(args.S, args.E0, args.Km, args.k)
    #print (v)



    d ={
            "S": args.S,
            "E0": args.E0,
            "Km": args.Km,
            "k": args.k,
            "v": v
        }

if args.save_file:
    with open('--save_file', 'w') as file:
        file.write(json.dumps(d, indent=2))