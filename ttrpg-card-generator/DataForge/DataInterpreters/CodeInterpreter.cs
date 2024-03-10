using System;
using System.Text.RegularExpressions;
using HtmlAgilityPack;

namespace DataForge.DataInterpreters
{
    public class CodeInterpreter
    {
        
        private HtmlDocument htmlDoc;
        protected HtmlNode strippedHtmlDocNode;

        public CodeInterpreter(string sourceCode, string strippedTag)
        {
            htmlDoc = new HtmlDocument();
            htmlDoc.LoadHtml(sourceCode);
            strippedTag = $"//{strippedTag}";
            strippedHtmlDocNode = htmlDoc.DocumentNode.SelectSingleNode(strippedTag);
        }

        // Strip list of strings and return it as a list of strings
        public static string PrettifyList(HtmlNodeCollection listToPrettify)
        {
            List<string> prettifiedList = new List<string>();
            foreach (HtmlNode node in listToPrettify)
            {
                prettifiedList.Add(GetText(node));
            }
            prettifiedList = prettifiedList.Select(item => item.Trim()).ToList();
            if (prettifiedList.Count == 1)
            {
                return prettifiedList[0];
            }
            return string.Join(", ", prettifiedList);
        }

        // Return the text of an element and replace the tags with a whitespace
        public static string GetText(HtmlNode element)
        {
            return Regex.Replace(element.InnerText.Trim(), @"\s{2,}", " ");
        }

        // Remove all comments from the given html code and return the cleaned html code
        protected static HtmlNode RemoveComments(HtmlNode htmlNode)
        {
            var comments = htmlNode.DescendantsAndSelf().Where(n => n.NodeType == HtmlNodeType.Comment).ToList();
            foreach (var comment in comments)
            {
                comment.Remove();
            }
            return htmlNode;
        }

        // Return a prettified version of the given html code
        protected static string PrettifyHtml(HtmlNode htmlNode)
        {
            htmlNode = RemoveComments(htmlNode);

            string prettyContents = htmlNode.OuterHtml;
            return prettyContents;
        }


        public string GetPrettySourceHtml()
        {
            return PrettifyHtml(htmlDoc.DocumentNode);
        }

        public string GetStrippedSourceHtml()
        {
            return strippedHtmlDocNode.OuterHtml;
        }

        public string GetPrettyStrippedSourceHtml()
        {
            return PrettifyHtml(strippedHtmlDocNode);
        }
    }
}