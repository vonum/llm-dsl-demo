from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader

APIKEY = "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"
loader = DirectoryLoader("./documents", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

# llm = OpenAI(openai_api_key=APIKEY)
# chat_model = ChatOpenAI(openai_api_key=APIKEY)

def run_query(query: str):
    query = f"""
        Transform the following text into Orus grammar if applicable:
        text:
        {query}
    """
    with get_openai_callback() as cb:
        response = index.query(query)
        print(query)
        print(response)
        print(cb)

# Success
query = "What is the swap count of uniswap, sushi and balancer on polygon and ethereum chain in the past 10 days?"
run_query(query)

query = "What is the price and market cap of usdc and maker in the past 3 years on ethereum chain?"
run_query(query)

query = "What is the transaction volume of usdc, maker and ether assets in the past 3 years on ethereum and polygon chain?"
run_query(query)

query = "What is the swap count of usdc, maker and ether pools on uniswap in the past 15 days?"
run_query(query)

query = "What is the price of usdt, link and wrapped bitcoin assets on polygon chain?"
run_query(query)

query = "What is the swap volume buy for usdc and maker on uniswap app on ethereum chain in the past 2 weeks?"
run_query(query)

query = "How much usdc and maker was bought on uniswap on ethereum chain in the past 2 weeks?"
run_query(query)

query = "What is the swap count of all balancer applications in the past 3 days"
run_query(query)

query = "What is the swap count of all balancer applications for usdc asset in the past 3 days"
run_query(query)

query = "What is the swap count of all balancer applications for usdc and weth pools in the past 3 days"
run_query(query)

query = "What is the swap count of uniswap dao in the past 3 days"
run_query(query)

query = "What is the swap count in ethereum ecosystem in the past 3 days"
run_query(query)

query = "What is the repay and borrow volume on aavev2 for all usdc pools in the past 2 years?"
run_query(query)

query = "What is the repay and borrow volume in usd on aavev2 for all usdc pools in the past 2 years?"
run_query(query)

query = "What is the liquidity of usdc asset on all aave protocols on polygon chain in the past 5 years?"
run_query(query)

query = "What is the lending rate and borrowing rate for usdc asset on aavev3 in the past 7 days?"
run_query(query)

query = "What is the lending rate and borrowing rate for wrapped bitcoin asset on aavev3 in the past 7 days?"
run_query(query)

# Failure
query = "When did we land on the moon?"
run_query(query)

query = "Generate a blog post about people with 20 words?"
run_query(query)

query = "Best way to hack pentagon?"
run_query(query)
