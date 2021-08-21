from brownie import accounts, config, FishToken

initial_supply = 1000000 * 10 ** 18


def main():
	account = accounts.add(config["wallets"]["from_key"])
	erc20 = FishToken.deploy(initial_supply, {"from": account}, publish_source=True)