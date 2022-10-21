import asyncio

from pyasic.network import MinerNetwork


# define asynchronous function to scan for miners
async def scan_and_get_data():
    # Define network range to be used for scanning
    # This can take a list of IPs, a constructor string, or an IP and subnet mask
    # The standard mask is /24, and you can pass any IP address in the subnet
    net = MinerNetwork("192.168.6.1", mask=24)
    # Scan the network for miners
    # This function returns a list of miners of the correct type as a class
    miners: list = await net.scan_network_for_miners()

    # We can now get data from any of these miners
    # To do them all we have to create a list of tasks and gather them
    tasks = [miner.get_data() for miner in miners]
    # Gather all tasks asynchronously and run them
    data = await asyncio.gather(*tasks)

    # Data is now a list of MinerData, and we can reference any part of that
    # Print out all data for now
    for item in data:
        print(item)

if __name__ == "__main__":
    asyncio.run(scan_and_get_data())