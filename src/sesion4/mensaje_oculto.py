# https://github.com/oskargicast/bamtang/tree/master/prob2

import string


MENSAJE_ENCRIPTADO = """
uid nx, aex jcdjipx iu wzux zp, ta wxtpa jtdaws, ai etkx vis.
dcos zyexdzaxr aex jxdw jezwipijes iu etkzyg nidx aety iyx hts
ai ri aex ptnx aezyg. z zyexdzaxr aeta jezwipijes udin wtdds htww,
hei zp ns exdi tqactwws. z htya ai ntfx dcos cpxdp udxx. z htya ai
gzkx aexn aex udxxrin ai qeiipx. jxijwx tdx rzuuxdxya. jxijwx qeiipx
rzuuxdxya qdzaxdzt. oca zu aexdx zp t oxaaxd hts tniyg ntys
twaxdytazkxp, z htya ai xyqicdtgx aeta hts os ntfzyg za qinuidatowx.
pi aeta'p heta z'kx adzxr ai ri.
z htya ai piwkx jdiowxnp z nxxa zy aex rtzws wzux os cpzyg qinjcaxdp,
pi z yxxr ai hdzax jdigdtnp. os cpzyg dcos, z htya ai qiyqxyadtax aex
aezygp z ri, yia aex ntgzqtw dcwxp iu aex wtygctgx, wzfx patdazyg hzae
jcowzq kizr  pinxaezyg pinxaezyg pinxaezyg ai pts, "jdzya exwwi hidwr."
z vcpa htya ai pts, "jdzya aezp!" z riy'a htya tww aex pcddicyrzyg
ntgzq fxshidrp. z vcpa htya ai qiyqxyadtax iy aex atpf. aeta'p aex otpzq
zrxt. pi z etkx adzxr ai ntfx dcos qirx qiyqzpx tyr pcqqzyqa.
scfzezdi ntapcniai. (hhh.tdaznt.qin/zyak/dcos)
"""

FREQ_CODE = "TEOIARNSHLMYUCWDGPFBVKJ".lower()


def obtiene_tabla_frecuencias(mensaje):
    """
    Contabilizar cuantas veces se repite un caracter.
    """

    freq_dict = {}  # freq_dict = dict()
    for letra in string.ascii_lowercase:
        repeticiones = mensaje.count(letra)
        if repeticiones:  # repeticiones != 0
            freq_dict[letra] = repeticiones
    return freq_dict


def ordena_diccionario_devuelve_cadena(diccionario):
    """
    Retorna una cadena ordenada basa en la tabla de frecuencias.
    """

    freq = sorted(diccionario, key=diccionario.get, reverse=True)
    freq = ''.join(freq)
    return freq


def desencripta(msg, code):
    """
    Desencripta el mensaje(msg) dado en base un codigo(code).
    """
    
    dic_freq = obtiene_tabla_frecuencias(msg)
    freq = ordena_diccionario_devuelve_cadena(dic_freq)
    mensaje = [''] * len(msg)
    for i, letra in enumerate(msg):
        index = freq.find(letra)
        if index == -1:
            mensaje[i] = letra
            continue
        mensaje[i] = code[index]
    return ''.join(mensaje)


def principal():
    mensaje_desencriptado = desencripta(MENSAJE_ENCRIPTADO, FREQ_CODE)
    print(mensaje_desencriptado)


if __name__ == '__main__':
    principal()