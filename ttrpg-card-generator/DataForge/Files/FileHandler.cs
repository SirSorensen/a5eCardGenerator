

namespace DataForge.Files
{
    public class FileHandler
    {
        private static string outputDirectory = "Outputs/";
        private static string scrapedDataOutputDirectory = $"{outputDirectory}ScrapedData/";

        // Returns the contents of a file as a string
        public string readFile(string absolutePath)
        {
            return System.IO.File.ReadAllText(absolutePath);
        }


        // Replaces the contents of a file with the given string and returns the new contents
        public string writeToFile(string absolutePath, string newContents)
        {
            System.IO.File.WriteAllText(absolutePath, newContents);
            return newContents;
        }

        public bool fileExists(string absolutePath)
        {
            return System.IO.File.Exists(absolutePath);
        }

        public string genDataDirectory(string cardType, FileType fileType, string contextName)
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
            

            return $"{scrapedDataOutputDirectory}{cardType}s/{codeType}/{contextName}{fileExtension}";
        }




    }


    public enum FileType
    {
        Text,
        Table,
        Card
    }

}


