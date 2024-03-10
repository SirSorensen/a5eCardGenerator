

using DataForge.DataInterpreters;
using DataForge.Files;

namespace DataForge.SourceCode
{
    public class SourceCode
    {
        public string updateTableSourceCode(string cardType, int pageNumber)
        {
            System.Console.WriteLine($"\nUpdating files for {cardType} table, page {pageNumber}. (See {WebsiteScraper.genTableUrl(cardType, pageNumber)} for source.)");
           
            // Scrape table source code if it doesn't exist yet
            string cardTableSourceCodePath = FileHandler.genCardListSourceCodeDirectory(cardType, pageNumber);
            string sourceCode;
            if (FileHandler.fileExists(cardTableSourceCodePath))
            {
                sourceCode = FileHandler.readFile(cardTableSourceCodePath);
            }
            else 
            {
                sourceCode = WebsiteScraper.scrapeTableSourceCode(cardType, pageNumber);
                FileHandler.writeToFile(cardTableSourceCodePath, sourceCode);
            }

            // Set up TableInterpreter
            TableInterpreter tableInterpreter = new TableInterpreter(sourceCode);

            // Prettify table source code
            string tablePrettyCodePath = FileHandler.genCardListSourceCodeDirectory(cardType, pageNumber, isPretty: true);
            string prettySourceCode = tableInterpreter.GetPrettySourceHtml();
            FileHandler.writeToFile(tablePrettyCodePath, prettySourceCode);


            // Generate/find table stripped code
            string tableStrippedCodePath = FileHandler.genCardListSourceCodeDirectory(cardType, pageNumber, isStripped: true);
            string strippedSourceCode = tableInterpreter.GetStrippedSourceHtml();
            FileHandler.writeToFile(tableStrippedCodePath, strippedSourceCode);

            // Prettify table stripped code
            string strippedPrettyCodePath = FileHandler.genCardListSourceCodeDirectory(cardType, pageNumber, isStripped: true, isPretty: true);
            string strippedPrettySourceCode = tableInterpreter.GetPrettyStrippedSourceHtml();
            FileHandler.writeToFile(strippedPrettyCodePath, strippedPrettySourceCode);


            return sourceCode;
        }
    }
}
