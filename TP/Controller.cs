using CalculatorApp.Models;
using Microsoft.AspNetCore.Mvc;
using System.Net.Security;
using System.Runtime.InteropServices;

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
            if (CalcState.IsValid)
            {
                switch (calc.Operation)
                {
                    case "+":
                        calc.result = calc.Operand1 + calc.Operand2;
                        break;
                    case "-":
                        calc.result = calc.Operand1 + calc.Operand2;
                        break;
                    case "*":
                        calc.result = calc.Operand1 * calc.Operand2;
                        break;
                }
            }
            return View(calc);
        }
    }
}
