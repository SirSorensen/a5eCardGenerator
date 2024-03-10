

namespace DataForge.Files
{
    public class FileHandler
    {
        private static string outputDirectory = "Outputs/";
        private static string scrapedDataOutputDirectory = $"{outputDirectory}ScrapedData/";

        // Returns the contents of a file as a string
        public static string readFile(string absolutePath)
        {
            return System.IO.File.ReadAllText(absolutePath);
        }


        // Replaces the contents of a file with the given string and returns the new contents
        public static string writeToFile(string absolutePath, string newContents)
        {
            System.IO.Directory.CreateDirectory(absolutePath.Substring(0, absolutePath.LastIndexOf('/')));
            System.IO.File.WriteAllText(absolutePath, newContents);
            return newContents;
        }

        public static bool fileExists(string absolutePath)
        {
            return System.IO.File.Exists(absolutePath);
        }

        public static string genDataDirectory(string cardType, FileType fileType, string contextName, bool isPretty = false, bool isStripped = false)
        {   
            string fileExtension = ".html";
            string codeType = "";
            
            switch (fileType)
            {
                case FileType.Text:
                    codeType = "Strings";
                    fileExtension = ".txt";
                    break;
                case FileType.Table:
                    codeType = "Tables";
                    break;
                case FileType.Card:
                    codeType = "SourceCode";
                    break;
            }

            if (isStripped) codeType += "/Stripped";
            if (isPretty) codeType += "/Pretty";
            
            return $"{scrapedDataOutputDirectory}{cardType}s/{codeType}/{contextName}{fileExtension}";
        }


        public static string genCardListSourceCodeDirectory(string cardType, int pageNumber, bool isPretty = false, bool isStripped = false)
        {
            return genDataDirectory(cardType, FileType.Table, $"page_{pageNumber}", isPretty, isStripped);
        }

    }


    public enum FileType
    {
        Text,
        Table,
        Card
    }

}


