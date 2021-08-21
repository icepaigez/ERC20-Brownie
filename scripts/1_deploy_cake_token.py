from brownie import accounts, config, CakeToken

initial_supply = 1000000
token_name = 'Cake Token' 
token_symbol = 'CAKE'

def main():
	account = accounts.add(config["wallets"]["from_key"])
	erc20 = CakeToken.deploy(initial_supply, token_name, token_symbol, {"from": account}, publish_source=True)