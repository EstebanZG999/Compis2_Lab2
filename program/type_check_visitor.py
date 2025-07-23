from visitor.SimpleLangParser import SimpleLangParser
from visitor.SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
    
  # Comparison: <, >, <=, >=
  def visitComparison(self, ctx: SimpleLangParser.ComparisonContext):
      left  = self.visit(ctx.expr(0))
      right = self.visit(ctx.expr(1))
      if isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
          return BoolType()
      raise TypeError(f"Unsupported operand types for {ctx.op.text}: {left} and {right}")

  # Logical: &&, ||
  def visitLogical(self, ctx: SimpleLangParser.LogicalContext):
      left  = self.visit(ctx.expr(0))
      right = self.visit(ctx.expr(1))
      if isinstance(left, BoolType) and isinstance(right, BoolType):
          return BoolType()
      raise TypeError(f"Unsupported operand types for {ctx.op.text}: {left} and {right}")

  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
