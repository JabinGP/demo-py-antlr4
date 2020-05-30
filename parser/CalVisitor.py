# Generated from Cal.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalParser import CalParser
else:
    from CalParser import CalParser

# This class defines a complete generic visitor for a parse tree produced by CalParser.

class CalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalParser#prog.
    def visitProg(self, ctx:CalParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#printExpr.
    def visitPrintExpr(self, ctx:CalParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#assign.
    def visitAssign(self, ctx:CalParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#blank.
    def visitBlank(self, ctx:CalParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#parens.
    def visitParens(self, ctx:CalParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#MulDiv.
    def visitMulDiv(self, ctx:CalParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#AddSub.
    def visitAddSub(self, ctx:CalParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#id.
    def visitId(self, ctx:CalParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#int.
    def visitInt(self, ctx:CalParser.IntContext):
        return self.visitChildren(ctx)



del CalParser