MakeYourTrip travel agency has developed a new Cab Service platform that integrates Google Maps technology with their proprietary cab booking system. This comprehensive solution enables customers to plan their travel itinerary through a streamlined process.
The new cab service platform offers several key features:

- Book a cab to your desired destination
- Cancel existing reservations when plans change
- Access detailed driver information

All these functions are conveniently accessible through Claude Desktop.

**Prerequisites:**
- Get a Google Maps API key by following the instructions [here](https://developers.google.com/maps/documentation/javascript/get-api-key#create-api-keys)
- Have nodejs installled in your local computer
- Have Claude Desktop installed


We will be using this MCP Server with Claude Desktop, for which we need to add the following in our `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "google-maps": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-google-maps"
      ],
      "env": {
        "GOOGLE_MAPS_API_KEY": "<YOUR GOOGLE MAPS API KEY HERE>"
      }
    },
    "cab-service": {
      "command": "C:\\Users\\Siddhant\\.local\\bin\\uv", // Absolute path to uv
      "args": [
        "--directory",
        "D:\\projects\\cab-service", // Absolute path to the MCP server
        "run",
        "main.py"
      ]
    }
  }
}
```

**Example Requests**
- I want to travel from Vadodara to Ahmedabad and have around 8 hours in which I plan to visit 3 must visit places in ahmedabad. Plan the trip accordingly, such that I can visit all the places within the given time-range of 8hrs. Also book the cabs for this trip.

- I'm visiting Delhi for a weekend. Create an itinerary for seeing major landmarks and arrange transportation between them.

- Help me find the best street food locations in Lucknow and create an efficient route with cab bookings between stops.