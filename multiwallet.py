

from bitcoinlib.wallets import Wallet
from eth_account import Account

def create_bitcoin_wallet(wallet_name):
    wallet = Wallet.create(wallet_name)
    return wallet

def create_ethereum_wallet():
    account = Account.create()
    return account.address, account.privateKey.hex()

if __name__ == "__main__":
    wallet_name = input("Enter a name for your Bitcoin wallet: ")
    bitcoin_wallet = create_bitcoin_wallet(wallet_name)
    print(f"Bitcoin Wallet '{wallet_name}' created with address: {bitcoin_wallet.get_key().address}")

    eth_address, eth_private_key = create_ethereum_wallet()
    print(f"Ethereum Wallet created with address: {eth_address} and private key: {eth_private_key}")
