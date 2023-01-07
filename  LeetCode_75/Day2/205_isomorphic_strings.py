def isIsomorphic(s: str, t: str) -> bool:
        s_orders = {}
        t_orders = {}
        for index, alphabats in enumerate(zip(s,t)):
            alpha_s, alpha_t = alphabats
            if alpha_s not in s_orders:
                s_orders[alpha_s] = []
            s_orders[alpha_s].append(index)
            if alpha_t not in t_orders:
                t_orders[alpha_t] = []
            t_orders[alpha_t].append(index)
            if s_orders[alpha_s] != t_orders[alpha_t]:
                return "false"
        return "true"

    
print(isIsomorphic(s="foo", t="bar"))