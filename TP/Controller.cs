using CalculatorApp.Models;
using Microsoft.AspNetCore.Mvc;
using System.Net.Security;
using System.Runtime.InteropServices;
using WebApplication1665.Models;

namespace WebApplication1665.Controllers
{
    public class HomeController : Controller
    {
        public ViewResult Index()
        {
            int hour = DateTime.Now.Hour;
            ViewBag.Greeting = hour < 12 ? "Доброе утро" : "Доброго дня";
            return View();
        }
        [HttpGet]
        public ViewResult RsvpForm()
        {
            return View();
        }
        [HttpPost]
        public ViewResult RsvpForm(CalculatorModel calc)
        {
            int selectedFunction = Convert.ToInt32(Request["calkey"]);

            switch (selectedFunction) {
                case 0:
                    calc.result = calc.Operand1 + calc.Operand2;
                    break;
                case 1:
                    calc.result = calc.Operand1 + calc.Operand2;
                    break;
                case 2:
                    calc.result = calc.Operand1 * calc.Operand2;
                    break;
            }
            return View(calc);
        }
    }
}
