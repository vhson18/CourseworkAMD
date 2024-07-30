namespace UrlShortenerApi.Models
{
    public class UrlMapping
    {
        public int Id { get; set; }
        public string ShortUrl { get; set; }
        public string OriginalUrl { get; set; }
    }
}
