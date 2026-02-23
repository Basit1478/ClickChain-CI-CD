import sys
from clickchain_service import ClickChainService

def main():
    print("========================================")
    print("  ClickChain Application Starting...   ")
    print("  Environment : UAT                    ")
    print(f"  Python Version: {sys.version.split()[0]}")
    print("========================================")

    service = ClickChainService()
    service.start()

if __name__ == "__main__":
    main()
