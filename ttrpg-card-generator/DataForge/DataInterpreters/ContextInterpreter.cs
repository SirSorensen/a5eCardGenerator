


using HtmlAgilityPack;
namespace DataForge.DataInterpreters
{
    public class ContextInterpreter : CodeInterpreter
    {
        public ContextInterpreter(string sourceCode) : base(sourceCode, "article")
        {
        }

        private string getContents(HtmlNode node)
        {
            if (node == null)
            {
                return "";
            }

            string elementText = GetText(node);
            string trimmedElementText = elementText.Trim();
            return trimmedElementText;
        }

        private List<string> extractContentList(string artVal, string tagType, string atrName)
        {
            HtmlNode foundNode = strippedHtmlDocNode.SelectSingleNode(artVal);
            return extractFieldItems(foundNode);
        }

        private List<string> extractFieldItems(HtmlNode node)
        {
            if (node == null) return new List<string>();
            

            HtmlNodeCollection fieldItems = node.SelectNodes("div");
            return fieldItems.Select(item => getContents(item)).ToList();
        }



    }
}