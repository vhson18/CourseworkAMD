using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using UrlShortenerApi.Services;

namespace UrlShortenerApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UrlShortenerController : ControllerBase
    {
        private readonly UrlShortenerService _service;

        public UrlShortenerController(UrlShortenerService service)
        {
            _service = service;
        }

        [HttpPost("shorten")]
        public async Task<IActionResult> ShortenUrl([FromBody] string originalUrl)
        {
            var shortUrl = await _service.ShortenUrlAsync(originalUrl);
            return Ok(new { shortUrl });
        }

        [HttpGet("{shortUrl}")]
        public async Task<IActionResult> RedirectToOriginalUrl(string shortUrl)
        {
            var originalUrl = await _service.GetOriginalUrlAsync(shortUrl);

            if (string.IsNullOrEmpty(originalUrl))
            {
                return NotFound();
            }

            return Redirect(originalUrl);
        }
    }
}
