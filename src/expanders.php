<?php

namespace Yay\DSL\Expanders;

use Yay\Engine;
use Yay\Token;
use Yay\TokenStream;

function base64(TokenStream $stream, Engine $engine): TokenStream
{
    $stream = \base64_encode($stream);

    return TokenStream::fromSource(
        $engine->expand($stream, "", Engine::GC_ENGINE_DISABLED)
    );
}
