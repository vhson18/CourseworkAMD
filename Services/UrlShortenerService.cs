using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using UrlShortenerApi.Data;
using UrlShortenerApi.Models;

namespace UrlShortenerApi.Services
{
    public class UrlShortenerService
    {
        private readonly UrlShortenerContext _context;
        private static readonly string BaseUrl = "http://short.url/";

        public UrlShortenerService(UrlShortenerContext context)
        {
            _context = context;
        }

        public async Task<string> ShortenUrlAsync(string originalUrl)
        {
            var existingMapping = await _context.UrlMappings
                .FirstOrDefaultAsync(m => m.OriginalUrl == originalUrl);

            if (existingMapping != null)
            {
                return BaseUrl + existingMapping.ShortUrl;
            }

            var shortUrl = GenerateShortUrl();
            var urlMapping = new UrlMapping
            {
                OriginalUrl = originalUrl,
                ShortUrl = shortUrl
            };

            _context.UrlMappings.Add(urlMapping);
            await _context.SaveChangesAsync();

            return BaseUrl + shortUrl;
        }

        public async Task<string> GetOriginalUrlAsync(string shortUrl)
        {
            var urlMapping = await _context.UrlMappings
                .FirstOrDefaultAsync(m => m.ShortUrl == shortUrl);

            return urlMapping?.OriginalUrl;
        }

        private string GenerateShortUrl()
        {
            return Guid.NewGuid().ToString("N").Substring(0, 6); // Example short URL generation
        }
    }
}
