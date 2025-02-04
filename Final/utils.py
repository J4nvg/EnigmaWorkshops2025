import os
from models import APIKeyModel
from asyncio import run


async def setup_api_key(api_key: APIKeyModel):
    os.environ[api_key.name] = api_key.key
    coded = "".join(['*' for _ in range(len(api_key.key[8:]))])
    full = api_key.key[:8] + coded
    print(f"{api_key.name} has been set up. {full}")


if __name__ == "__main__":
    api_key = {
        "name": "VERY_COOL_API_KEY",
        "key": "sodfjhosdjfwe[pofk[pkgppowjed[kbvnuiksdkgvjewpofk"
    }
    run(setup_api_key(api_key))

