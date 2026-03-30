using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace CalculatorApp.Models
{
    public class CalculatorModel
    {
        public decimal Operand1 { get; set; }
        public decimal Operand2 { get; set; }
        public string Operation { get; set; }
        public decimal result { get; set; }
    }
