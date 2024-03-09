using System.Text.RegularExpressions;

namespace DataForge.DataStructures
{
    public class Card
    {
        public string title;
        public string name;

        public Card(string title, string sourceCode)
        {
            this.title = title;

            this.name = ToContextName(title);
            if (Globals.debug) Console.WriteLine($"Making a {GetType().Name}! {name}");

            SetFields(sourceCode);
            SetTextFields();
        }

        protected void SetFields(string sourceCode)
        {
            throw new NotImplementedException();
        }

        protected void SetTextFields()
        {
            throw new NotImplementedException();
        }

        public static string ToContextName(string inputStr)
        {
            string contextName = inputStr.ToLower();
            contextName = Regex.Replace(contextName, @"[^\w\d]", "_");
            return contextName;
        }

        public override string ToString()
        {
            List<string> fieldStrings = new List<string>();

            foreach (var field in GetType().GetFields())
            {
                if (!field.Name.StartsWith("_"))
                {
                    var fieldValue = field.GetValue(this);
                    if (fieldValue is List<object>)
                    {
                        foreach (var itemValue in (List<object>) fieldValue)
                        {
                            fieldStrings.Add($"{field.Name}: {itemValue}");
                        }
                    }
                    else
                    {
                        fieldStrings.Add($"{field.Name}: {fieldValue}");
                    }
                }
            }

            return string.Join("\n\n", fieldStrings);
        }
    }
}

