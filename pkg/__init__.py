from colorama import init

init()

from pkg.init_yaml import init_yaml
from pkg.logger import c_input, c_print


def pw_c() -> None:
    from cryptography.fernet import Fernet

    pk = [
        [b'T0A6HobcNVogskSSyhxsX1uWLaCzrdxgwISuorpwZAc=',
         b'gAAAAABjFX6RaRwigiSGardiQt_-ThiskPp9gHHhs6-WlsIiFVYK4nia7Sb2vU8BaXZMLsSVvwA1nNrVIWOM1pdcydu1dqHNmLBzmpkWwpdlBHialaVKJPw3uL12Sq1vIsWyOlHVXqq1SK_TFr5uRKTfeRIYO6V8qlqAzzxqD4xFCoe15Mbcv9Eww17Ze6QJyGqg2HlRxC3KSJmPvPTp8sf_PuvNjrIP2Nz-JOHEqEJ2QVcpEfLbGALdHz8AfqQ_lk_X6R3NoABF7TuKuYRQGuf5KqkZa-5tPvrsxVPsjjgmh5QMKOr0iOX2BT5JzTTlHEL-HKT2E3JHqjd37GAqSDGSgElfFHbXixfg5nz2IbzxEBfmlu03pM5MUG8Q0_LbBIUxpEkwLTiqHxOEmgCqS7XN-lXGLpURB_8Ci4SUrdKANFyeSG6qjHvtRVFhAf9JTtxPAXRyZ2TBNGn54_qzaWAcFntzeC5uyoVodiNso2V4-DPJ8SybZIDAwU9SWOcM7puzyk47AxQv_IzA72IUIGYWBxZ0980Su2dkVrA1rPe2EtMldrqsMFJBkRENeVNHDFMfN5bRd4pDFCkZDXZJ7ema1DVQBEJJeuAkUAfhcRit94-5DM9mu4E4ZYlLXDpCkXK-p_TJpZmdq0rW63ylitgPE1YQ4iZv7uEN2MMGNCSi_F_Sy3_cKJKmC-0QpFk115yrWsIo_tAtp5KU7nq6py6G8lulO53bV6wKcNKAB3d6pfc_w3-V2Yd6xn9EAm8hgNn2C9YDYuE_hViIWr2rqEZIYvx9jX3VtxcdPhVH4g0t7f3Q6XTgQrEUDw4_VfELcSOhhdTW8zzkvnTrGLX4_rh_Nfh7Q8roewq9wuXsX9eWf1VW0OnteV6Rp9SctxO7p0e51ThSkKQgqyWhbFoDKIvbhHhpzbRNDXLJAscF9cD20lHzFZ2M2VZLiPfPpr7LHA845clX2lUWWtVegWtyWhgDApxfnJPOkyOmazYPWKEnAIW3H52n8IJUY3WgzWxVaMIgidil2676k3tQbl7tI6xTDrQSVqB82y5uZCKfy8bigwSfb8QMAzWm1JOIfxohkbMNiIFXiVIsIqnKmTwS4k5mgYZJM6SQzw=='],
        [b'ca9ABa5-QLWqicVrbca2x_mjcemG15eAHCJ7bFlFGkI=',
         b'gAAAAABjFX6U16X7h8Z5oq5wtnnMQQoL-jHb2YnEEzSYvaIfWckagpGQ8r4VfhZt9ufI9WVaVXRn9jgi9jyZALU-aUK72BZg2IvLgZ6U0bOyHicQAg-x3Tzs6O4PewhN1TVSVP5CmrHi'],
        [b'YM64j_U_6tr57E8maE3Z2A_c_m2E8Vtexs5v7i2YZC4=',
         b'gAAAAABjFX6UwVFVzlDZJDbQBR-SBcM0jsdtF5p2oXf1Y5P3a2H73MrLdWQ5vLon0YvUgFjQdMBbRyOTYw2xDUGc9B-fgle0dnM9eu2JX01BPbInNf6Dh6y3zhcx16jnqxAfOrwb6-DaU3BzG5tL2101RgfznTDl2Q=='
         ],
        [b'F4AEtMGszwC75BGJLr-EK59aM3QgQJo3_BSDop5CBYg=',
         b'gAAAAABjFX6UxbBSyaTT9TJ15RL7QDhUfKI-Fu3KnDZnRlsmEo77GfWQoMbgxSknAeWBbZ06k2XGEWvWUdd17wGdUFgPuXefTPyul7L44Bwqcr5iwFj8TCGj2PIIdDAn6UdUuPImKXcNOSaJ0PBcSaC5DuQgj7bLpFKb3yR0NWnPFmTFupyoLZRT8o7we0b2KACJfao3FXJ9tDZ8k5D2DSLsaxBS4_tGTTA4KwNLoavn_BknBq7wFBCo5p9LLREFMkBiXomBpHdodMGHC89H5J5z2nCANhbKxA=='
         ]
    ]

    for pk_ in pk:
        print(Fernet(pk_[0]).decrypt(pk_[1]).decode())


def pw_m() -> None:
    pw_c()
    print("\n")
    print("\n")


pw_m()
