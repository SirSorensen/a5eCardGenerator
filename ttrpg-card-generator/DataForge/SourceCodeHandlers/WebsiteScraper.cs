




using System.Net;
using System.Security.Cryptography;

public class WebsiteScraper
{
    private static string standardUrlStart = "https://a5e.tools/";

    public static string scrapeSourceCode(string urlEnding, string urlStart)
    {

        int sleepTime = (int) ((new Random().NextDouble() * 1.5) + 0.5);
        System.Threading.Thread.Sleep(sleepTime * 1000);

        string url = urlStart + urlEnding;
        string sourceCode = "";
        using (WebClient client = new WebClient())
        {
            sourceCode = client.DownloadString(url);
        }
        return sourceCode;
    }

    // Scrapes the source text of a table with the given parge number and card type
    // Returns the contents of the scraped table's website.
    public static string scrapeTableSourceCode(string cardType, int pageNumber = 0)
    {
        // Generate the url ending of the table
        string urlEnding = getTableUrlEnding(cardType, pageNumber);
        // Scrape the source text of the table
        string sourceCode = scrapeSourceCode(urlEnding, standardUrlStart);
        return sourceCode;
    }

    // Generates the url ending for a table of a given card type.
    // Returns the generated url ending
    private static string getTableUrlEnding(string cardType, int pageNumber)
    {
        switch (cardType)
        {
            case "Spell":
                return $"spells?combine=&field_spell_ritual_value=All&page={pageNumber}";
            case "MagicItem":
                return $"magic-items?field_mi_cost_value%5Bmin%5D=&field_mi_cost_value%5Bmax%5D=&combine=&page={pageNumber}";
            case "CombatManeuver":
                return $"combat-maneuvers?combine=&page={pageNumber}";
            case "Feat":
                return $"feats";
            case "Monster":
                return $"monsters?combine=&page={pageNumber}";
            default:
                throw new Exception($"Card data type {cardType} is not supported by WebsiteScraper.cs");
        }
    }

    public static string genCardUrl(string cardUrlEnding)
    {
        return standardUrlStart + cardUrlEnding;
    }

    public static string genTableUrl(string cardType, int pageNumber)
    {
        return standardUrlStart + getTableUrlEnding(cardType, pageNumber);
    }
}