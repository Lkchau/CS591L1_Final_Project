import tokenize

def comments(code, funcLineNo):
    commentLines = []
    commentMap = {}
    with open(code, 'r') as file:
        for toktype, tok, start, end, line in tokenize.generate_tokens(file.readline):
            if toktype == tokenize.COMMENT:
                strippedToken = tok.replace('#','').strip()
                if(strippedToken == "comment"):
                    commentLines.append(end[0])
                    if(end[0] + 1 in funcLineNo):
                        commentMap.update({end[0] : end[0]+1})
                    
        return commentLines, commentMap